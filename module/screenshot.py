import os


def use_aquatone(out_dir):
    responsive_url_list = out_dir + 'responsive.txt'

    os.system('cat {} | aquatone -chrome-path ~/chromium-latest-linux/latest/chrome -out {} -threads 5 -silent'
              .format(responsive_url_list, out_dir))
    return


if __name__ == '__main__':
    use_aquatone('~/recon_result/certik.io/Mar-13-2020/')
