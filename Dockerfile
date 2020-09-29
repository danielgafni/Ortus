FROM continuumio/miniconda3

WORKDIR /ortus
COPY . .

RUN echo SECRET_KEY=$(openssl rand -hex 50) > .env.local
RUN echo SECRET_VALIDATOIN_KEY=$(openssl rand -hex 50) >> .env.local

RUN conda update -n base -c defaults conda
RUN conda install --file conda-requirements.txt -c conda-forge
RUN echo ". ~/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate" >> ~/.bashrc
EXPOSE 3000
CMD ["python", "app.py"]