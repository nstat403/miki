import datetime

if __name__ == "__main__":

    #print("tedt")
    now=datetime.datetime.now()
    today=datetime.datetime.strftime(now,"%Y%m%d_%H%M%S")
    print(today)

