#!/usr/bin/env python3
"""Automated film QA: extract specs, detect cuts, extract frames."""
import subprocess, sys, os, json, re

def get_specs(path):
    r = subprocess.run(['ffprobe','-v','error','-show_entries',
        'format=duration,size,bit_rate',
        '-show_entries','stream=codec_type,width,height,r_frame_rate',
        '-of','default=noprint_wrappers=1', path],
        capture_output=True, text=True)
    return r.stdout.strip()

def detect_cuts(path, threshold=0.25):
    r = subprocess.run(['ffmpeg','-i',path,'-vf',
        f"select='gt(scene,{threshold})',showinfo",'-f','null','-'],
        capture_output=True, text=True, stderr=subprocess.STDOUT)
    times = re.findall(r'pts_time:([0-9.]+)', r.stdout)
    return [float(t) for t in times]

def extract_frames(path, outdir, timestamps):
    os.makedirs(outdir, exist_ok=True)
    for i, t in enumerate(timestamps):
        subprocess.run(['ffmpeg','-y','-v','error','-ss',str(t),
            '-i',path,'-frames:v','1','-q:v','3',
            f'{outdir}/key_{t}s.jpg'], capture_output=True)

def contact_sheet(path, outdir, fps=10, total_dur=15, cols=5, rows=2):
    os.makedirs(outdir, exist_ok=True)
    subprocess.run(['ffmpeg','-y','-v','error','-i',path,'-vf',
        f'fps={fps}/{total_dur},scale=400:-1,tile={cols}x{rows}',
        '-frames:v','1',f'{outdir}/sheet.jpg'], capture_output=True)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: film_qa.py <video.mp4> [output_dir]")
        sys.exit(1)
    video = sys.argv[1]
    outdir = sys.argv[2] if len(sys.argv) > 2 else 'qa_frames'
    
    print("=== Technical Specs ===")
    print(get_specs(video))
    
    print("\n=== Scene Cuts ===")
    cuts = detect_cuts(video)
    print(f"{len(cuts)} cuts detected: {cuts}")
    if cuts:
        durations = [round(cuts[i+1]-cuts[i],2) for i in range(len(cuts)-1)]
        durations.append(round(float(get_specs(video).split('\n')[0].split('=')[1]) - cuts[-1], 2))
        print(f"Shot durations: {durations}")
        print(f"Average: {sum(durations)/len(durations):.2f}s")
    
    mid_cuts = [cuts[i] + (cuts[i+1]-cuts[i])/2 for i in range(min(len(cuts)-1, 4))]
    extract_frames(video, outdir, [0.5] + mid_cuts + [cuts[-1]+1 if cuts else 13])
    contact_sheet(video, outdir)
    print(f"\nFrames saved to {outdir}/")
