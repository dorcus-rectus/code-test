#pip install unstructured
#pip install networkx
#pip install pandas
#pip install openpyxl

from langchain.document_loaders import UnstructuredExcelLoader
from langchain.prompts import PromptTemplate
from langchain.llms import Bedrock

prompt = '''
Human: あなたはAWSのエキスパートです。指定された設計書のデータに基づき、
コードを作成してください。コードの種類は、Lambdaのコード、テストコード、
AWS SAMで必要なtemplate.yamlです。
<document>
{document}
</document>
Assistant:
'''

inference_modifier = {'max_tokens_to_sample':4096, 
                      "temperature":0.5,
                      "top_k":250,
                      "top_p":1,
                      "stop_sequences": ["\n\nHuman"]
                     }

llm = Bedrock(
    region_name="us-east-1",
    model_id="anthropic.claude-v2:1",
    model_kwargs = inference_modifier
)

loader = UnstructuredExcelLoader("設計書.xlsx", mode="elements")
docs = loader.load()
data = [str(doc.page_content) for doc in docs]

print(llm(prompt.format(document="\n".join(data))))