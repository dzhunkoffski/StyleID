import os
import argparse
import subprocess

def main(opt):
    styles_dir = [
        f for f in os.listdir(opt.styles) if os.path.isdir(os.path.join(opt.styles, f))
    ]
    print(f'All styles: {styles_dir}')
    base_cmd = [
        'python', 'run_styleid.py',
        '--cnt', opt.content,
        '--gamma', '0.75',
        '--T', '1.5',
        '--precomputed', ''
    ]
    for style in styles_dir:
        print(f'==== PROCESSING STYLE {style} ====')
        cmd = base_cmd + [
            '--sty', os.path.join(opt.styles, style), '--output_path', os.path.join(opt.output_path, style)
        ]
        print(f'==== CMD: {" ".join(cmd)}')
        subprocess.run(cmd)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--content')
    parser.add_argument('--styles')
    parser.add_argument('--output_path')
    opt = parser.parse_args()

    main(opt)
    print('+++++ FINISHED +++++')
