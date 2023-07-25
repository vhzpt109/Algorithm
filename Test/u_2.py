data_path = 'jobs.csv'


class SparkTask:
    def __init__(self, spark_session):
        self.job_counts_dict = None
        self.sc = spark_session.sparkContext
        self.spark = spark_session

    def group_sort(self, input_path):
        # Read CSV file
        rdd = self.sc.textFile(input_path)

        # Remove the header
        header = rdd.first()
        rdd = rdd.filter(lambda line: line != header)

        # Split each line by comma and map job to a tuple (job, 1)
        rdd = rdd.map(lambda line: (line.split(",")[1], 1))

        job_counts = rdd.reduceByKey(lambda a, b: a + b)

        # Swap job and count for sort by count => exam (3, Dancer)
        count_jobs = job_counts.map(lambda x: (x[1], x[0]))

        # Sort by key (count) in ascending order, then reswap
        sorted_counts = count_jobs.sortByKey().map(lambda x: (x[1], x[0]))

        # Collect RDD into a dictionary
        self.job_counts_dict = {k: v for k, v in sorted_counts.collect()}

        return self.job_counts_dict