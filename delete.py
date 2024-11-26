import boto3

# Crie um cliente SNS
sns_client = boto3.client('sns')

# ARN do tópico que você criou
topic_arn = 'arn:aws:sns:us-east-1:311351879181:TopicoMichelleteste'

# Excluindo o tópico SNS
response = sns_client.delete_topic(TopicArn=topic_arn)

# Verifique a resposta
print(f'Tópico excluído: {response}')
