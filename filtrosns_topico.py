import boto3

# Criar o cliente SNS
sns_client = boto3.client('sns')

def create_topic(topic_name):
    """Cria um tópico SNS."""
    response = sns_client.create_topic(Name=topic_name)
    topic_arn = response['TopicArn']
    print(f"Tópico criado com ARN: {topic_arn}")
    return topic_arn

def subscribe_to_topic(topic_arn, protocol, endpoint, filter_policy=None):
    """Assina um endpoint ao tópico com um filtro opcional."""
    attributes = {}
    if filter_policy:
        attributes['FilterPolicy'] = filter_policy
    
    response = sns_client.subscribe(
        TopicArn=topic_arn,
        Protocol=protocol,
        Endpoint=endpoint,
        Attributes=attributes
    )
    print(f"Assinatura pendente para {endpoint}. Confirme para ativar.")
    return response['SubscriptionArn']

def send_test_message(topic_arn, message, subject=None):
    """Envia uma mensagem de teste para o tópico."""
    response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject=subject
    )
    print("Mensagem enviada com sucesso!")
    return response

if __name__ == "__main__":

    # Criar o tópico
    topic_name = "TopicoMichelleteste"
    topic_arn = create_topic(topic_name)

    
# Criar assinatura com filtro e-mail

email = "email@mail.com"
email_filter_policy = '{"type": ["email"]}'
subscribe_to_topic(topic_arn, "email", email, email_filter_policy)

# Enviar mensagem de teste
test_message = '{"type": "email", "content": "Mensagem para email"}'



# Criar assinatura com filtro sms
    
sms = "+550001234560"  
sms_filter_policy = '{"type": ["sms"]}'    
subscribe_to_topic(topic_arn, "sms", sms, sms_filter_policy)

# Enviar mensagem de teste
send_test_message(topic_arn, test_message, subject="Teste SNS")
