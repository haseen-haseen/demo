# ######   ----------------------multithreading---------------------------------------
# import threading
# from concurrent.futures import ThreadPoolExecutor
# import time
# def thred(sec):
    
#     time.sleep(sec)
#     print(f" sleep for time {sec}")
#     return sec

# def fun():
#     time1=time.perf_counter()
#     # thred(2)

#     t1=threading.Thread(target=thred,args=[2])
#     t1.start()
#      # t1.join()
#     time2=time.perf_counter()
#     print(time2-time1)
# def poolingDemo():
#   with ThreadPoolExecutor(max_workers=1) as executor:
#     # future = executor.submit(thred,2)
#     # future1 = executor.submit(thred,2)
#     # print(future.result())
#     # print(future1.result())


#     l = [3, 5, 1, 2]
#     results = executor.map(thred, l)
#     for result in results:
#       print(result)
# poolingDemo()


######   ----------------------multiProcessing---------------------------------------

import multiprocessing
import requests
def downloadfile(url,name):
    res=requests.get(url)
    open(f"images/file{name}.jpg","wb").write(res.content)


if __name__ == '__main__':

    url = "https://picsum.photos/200/300"
    pros=[]
    for i in range(3):
        # downloadfile(url,i)
        p=multiprocessing.Process(target=downloadfile,args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
            

