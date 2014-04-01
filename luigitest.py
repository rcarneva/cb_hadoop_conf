import luigi
import luigi.hadoop
import luigi.hdfs

class WCInput(luigi.ExternalTask):
    def output(self):
        return luigi.hdfs.HdfsTarget("input.txt")

    def requires(self):
        return None

class WordCount(luigi.hadoop.JobTask):
    def output(self):
        return luigi.hdfs.HdfsTarget("testout")

    def requires(self):
        return WCInput()

    def mapper(self, line):
        for word in line.split(" "):
            yield word, 1

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    luigi.run()
