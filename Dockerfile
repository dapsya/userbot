#==============×==============#
#      Created by: Alfa-Ex
#=========× AyiinXd ×=========#

FROM ayiinxd/ayiin-userbot:buster

RUN git clone -b Senja-Userbot https://github.com/inisenja/Senja-Userbot /home/senjauserbot/ \
    && chmod 777 /home/senjauserbot \
    && mkdir /home/senjauserbot/bin/

COPY ./sample_config.env ./config.env* /home/senjauserbot/

WORKDIR /home/senjauserbot/

RUN pip install -r requirements.txt

CMD ["bash","start"]
