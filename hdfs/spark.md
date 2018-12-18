## 





$ ./bin/spark-submit --class org.apache.spark.examples.SparkPi \
    --master yarn \
    --deploy-mode cluster \
    --driver-memory 2g \
    --executor-memory 1g \
    --executor-cores 1 \
    --queue default \
    examples/jars/spark-examples*.jar \
    10




spark-shell --master yarn --deploy-mode client



spark-shell --driver-memory 512M --master yarn --deploy-mode client



