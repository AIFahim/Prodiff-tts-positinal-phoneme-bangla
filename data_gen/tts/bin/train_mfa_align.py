import subprocess
from utils.hparams import hparams, set_hparams
import os


def train_mfa_align():
    CORPUS = hparams['processed_data_dir'].split("/")[-1]
    print(f"| Run MFA for {CORPUS}.")
    NUM_JOB = int(os.getenv('N_PROC', os.cpu_count()))
    subprocess.check_call(f'CORPUS={CORPUS} NUM_JOB={NUM_JOB} bash mfa_usr/run_mfa_train_align.sh', shell=True)


if __name__ == '__main__':
    set_hparams(print_hparams=False)
    train_mfa_align()

# python data_gen/tts/runs/train_mfa_align.py