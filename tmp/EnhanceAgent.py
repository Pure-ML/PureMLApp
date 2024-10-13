import pandas as pd
import json

class EnhanceAgent:
    def __init__(self, rag_workflow):
        self.rag_workflow = rag_workflow

    @staticmethod
    def get_unique_values_by_index(dataset: pd.DataFrame, column_index: int):
        return dataset.iloc[:, column_index].unique()

    @staticmethod
    def update_column_with_mapping(df, col_idx, mapping):
        df.iloc[:, col_idx] = df.iloc[:, col_idx].map(mapping)
        return df

    async def enhance_column(self, dataset: pd.DataFrame, column_idx: int):
        uniq = EnhanceAgent.get_unique_values_by_index(dataset, column_idx)
        quote = list(map(lambda x: f"'{x}'", uniq))
        mk_str = ', '.join(quote)
        query_str = (
            f"I have a dataset of [{mk_str}]. Could you spot the same instances and build a map to remove duplicates? Return only json mapping, no other text."
        )
        response = await self.rag_workflow.run(
            query_str=query_str
        )
        mapping = json.loads(response.strip())
        print(f"Updating column '{column_idx}' with mapping {mapping}")
        dataset = EnhanceAgent.update_column_with_mapping(dataset, column_idx, mapping)

        return dataset
