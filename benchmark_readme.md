# How to benchmark

1. Follow instructions from `README.md` on how to setup the project.
2. Install `gdown` to download benchmark dataset:
```bash
pip install gdown
```
3. Download dataset:
```bash
gdown 1Q_jbI25NfqZvuwWv53slmovqyW_L4k2r
```
4. Unzip dataset:
```bash
unzip StyleBench.zip -d StyleBench
```
5. Run inference script:
```bash
python3 -u run_all_styles.py --content StyleBench/content --styles StyleBench/style --output_path output
```