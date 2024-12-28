from fontTools.ttLib.tables.E_B_L_C_ import sbitLineMetricsFormat
from pyhton:3.9.19-slim
RUN pip install streamlit
RUN mkdir /myapp
COPY . .
EXPOSE 8501

CMD ['streamlit','run','etl.py']