# Pet Service

This is an example of python project using flask and DynamoDB with boto3

## How to Run

1.Install dependencies

```bash
$ pip install -r requirements.txt
```

3.Run DynamoDBLocal using podman or docker

```bash
$ pdoman-compose up -d
```


2.If you are using Linux run

```bash
$ sudo chmod 777 ./docker/dynamodb
```

3.Create Pet Table

```bash
$ aws dynamodb \
 create-table --table-name Pets \
 --attribute-definition AttributeName=id,AttributeType=S \
 --key-schema AttributeName=id,KeyType=HASH \
 --billing-mode PAY_PER_REQUEST \
 --endpoint http://localhost:8000 \
 --region sa-east-1
```

4.Run application

```bash
python3 main.py
```

5.Send a new request

```bash
curl --request POST \
  --url http://localhost:8080/pets/v1 \
  --header 'Content-Type: application/json' \
  --data '{
	"name": "Mathias",
	"type": "DOG",
	"date_of_birth": "2022-04-01"
}'
```