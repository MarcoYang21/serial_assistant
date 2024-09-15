# src/core/data_processor.py
import rx
from rx import operators as ops

class DataProcessor:
    def __init__(self):
        self.data_subject = rx.subject.Subject()

    def process_data(self, data):
        self.data_subject.on_next(data)

    def get_observable(self):
        return self.data_subject.pipe(
            ops.map(lambda x: x.upper()),  # 例如，將所有數據轉換為大寫
            ops.filter(lambda x: len(x) > 0)  # 過濾掉空字符串
        )
