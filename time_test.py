import time
import schedule

# time1 = time.time()
# time2 = time.ctime()
# time3 = time.localtime()
# time4 = time.gmtime()
# time5 = time.asctime()
# time6 = time.mktime(time3)
# time7 = time.strftime("%Y-%m-%d %H:%M:%S", time3)
# time8 = time.strptime("2021-10-15 14:00:00", "%Y-%m-%d %H:%M:%S")

# print(f"time1: {time1}")
# print(f"time2: {time2}")
# print(f"time3: {time3}")
# print(f"time4: {time4}")
# print(f"time5: {time5}")
# print(f"time6: {time6}")
# print(f"time7: {time7}")
# print(f"time8: {time8}")

def job():
    print("I'm working...")
    return

schedule.every().day.at("10:38:00").do(job)

while True:
    schedule.run_pending()
    # time.sleep(1)

