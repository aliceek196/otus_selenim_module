FROM python3.8-alpine
WORKDIR /OpenCart
COPY requirments.txt
RUN pip install -U pip
RUN pip install -r requirments.txt
COPY ..
CMD ["pytest", "--browser", "chrome", "--base_url", "https://demo.opencart.com/"]
