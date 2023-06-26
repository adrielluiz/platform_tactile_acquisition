import logging

logging.basicConfig(format='[%(levelname)s] %(asctime)s %(message)s',
                    level=logging.INFO,datefmt='%Y-%m-%d %H:%M:%S', encoding = "UTF-8",
                        handlers=[ logging.FileHandler("logs.log"), logging.StreamHandler()]
                    )