import os
import time


class servelog:
    def option_file(self):
        from_file = "/Users/huangzw/me/logdeal/service.log.2022-08-17";
        to_file = "/Users/huangzw/me/logdeal/service.log"
        len = 0

        with open(from_file,'r') as fr , open(to_file, 'a') as wf:
            for line in fr:
                len += 1
                wf.writelines(line)
                wf.flush()
                time.sleep(5)
                print(line,sep='\n')
                if len % 100000 == 0 :
                    wf.close()
                    over_file = f"/Users/huangzw/me/logdeal/service.log.{len}"
                    os.rename(to_file, over_file)
                    wf =  open(to_file, 'a')


if __name__ == "__main__":
    servelog = servelog()
    servelog.option_file()







