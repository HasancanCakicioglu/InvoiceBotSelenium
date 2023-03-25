


def tryExceptHelperFunc(job):
    while True:
        try:
            job()
            break
        except Exception as e:
            print("3 except = "+str(e))
            pass
