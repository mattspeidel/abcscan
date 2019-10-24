FROM python:3
ADD scan.py /
ADD instock.txt /
ADD skulist.txt /
RUN pip install requests
RUN pip install twilio
RUN pip install schedule
# ENV TWILSID textgoeshere
# ENV TWILTOKEN textgoeshere
# ENV MYTWILNUMBER textgoeshere
# ENV MYPHONENUMBER textgoeshere
CMD [ "python", "./scan.py" ]