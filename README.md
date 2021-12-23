# 2021-12-37-Predicting-Real-Time-Stock-Index-Using-Tweet

Please note, the path or directory name for some variables in our program in which they loads data from, may have changed. Please change accordingly if you get some error.

To reproduce our results in during training. Please follow the steps below:
1. run twitter_client and spark_test once for a streaming period of your choice. This determines how many data you will have for pretaining
2. run bootstrap to increase data volume and update file_lst.pkl (For now, using the existent lst.pkl may yield an error as we modified the organization of this project, directory name may have changed. However, if you follow  the given steps, there should be no problem)
3. run pretraining to reproduce our model

To reproduce our results in the actual real-time prediction. Please follow the steps below:
1. Set up and make kafka and zookeeper running on the clusters your are using
2. Change time-interval to your choice in the spark_actual, online_prediction, update_model
3. Start twitter_client, get_price spark_actual, online_prediction, update_model simultaneously.
4. Run our visualization program to query and see results.
