FROM continuumio/miniconda3

WORKDIR /ortus
COPY . .

RUN conda update -n base -c defaults conda
RUN conda install --file conda-requirements.txt -c conda-forge
RUN echo ". ~/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc
RUN echo "conda activate" >> ~/.bashrc
CMD ["python", "app.py"]