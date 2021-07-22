# API REST - Serverless - Parrot

Esta API permite crear ordenes y usuarios para un restaurant.

## Estructura

Este proyecto esta separado por modulos, los modulos son `users`, `orders` y `authorizer`

## Casos de uso

- API for a Web Application
- API for a Mobile Application

## Setup

### NodeJs y npm

```bash
# Guia https://nodejs.org/en/download/package-manager/

# Usando Ubuntu
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Repositorio

```bash
# Clonar repositorio
git clone [repositorio]
cd [directory]

```

### AWS CLI 2

```bash
# Usar la siguiente guia dependiendo del sistema operativo
https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
```

Se necesita tener cuenta de aws con permisos `full access` de `lambda`
Nota: solo se necesita para poder subir el proyecto a una `lambda`


### Scripts
```bash
npm install -g serverless
npm install jsonwebtoken --save
pip3 install boto3
```

Ejecución de ambiente *local* descomentar las lineas de `plugins` en el archivo `serverelss.yml` y correr la siguientes lineas:
```bash
#Asegurarse que este instalado Java par el funcionamiento local de dynamob
sudo apt-get install default-jre

#plugin para correr serverless offline
npm install serverless-offline

#plugin para correr dynamodb de manera local
npm install serverless-dynamodb-local
sls dynamodb install
sls dynamodb start --migrate
```

## Herramientas

Las siguientes herramientas son usadas a lo largo del proyecto, esta descrita su funcionabilidad y en algunas un link para ver su documentación general

### Serverless

[![serverless](http://public.serverless.com/badges/v3.svg)](http://www.serverless.com)
Framework que permite crear funciones lambda y poderlas subir a AWS
<https://www.serverless.com/framework/docs/>

### DynamoDB

Servicio de base de datos NoSQL

<https://aws.amazon.com/es/dynamodb>

<https://docs.aws.amazon.com/dynamodb/index.html>

## Deploy

Para hacer deploy a AWS con un perfil especifico

```bash
serverless deploy --aws-profile xxxx
```

El resultado será similar a lo siguiente:
```bash
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service parrot-api-test.zip file to S3 (138.88 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..........................................................................
Serverless: Stack update finished...
Service Information
service: parrot-api-test
stage: dev
region: us-west-2
stack: parrot-api-test-dev
resources: 79
api keys:
  APIKEY-PARROT-TEST: xxxxxxxxxxxxxxxxxxxxxx
endpoints:
  POST - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/users
  GET - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/users
  GET - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/users/{email}
  POST - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders
  GET - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders
  GET - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders/{id}
  PUT - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders/{id}
  DELETE - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders/{id}
  GET - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/orders/report/{start_date}/{end_date}
  POST - https://xxxxxxxx.execute-api.us-west-2.amazonaws.com/dev/login
functions:
  createUser: parrot-api-test-dev-createUser
  getUsers: parrot-api-test-dev-getUsers
  getUser: parrot-api-test-dev-getUser
  createOrder: parrot-api-test-dev-createOrder
  getOrders: parrot-api-test-dev-getOrders
  getOrder: parrot-api-test-dev-getOrder
  updateOrder: parrot-api-test-dev-updateOrder
  deleteOrder: parrot-api-test-dev-deleteOrder
  report: parrot-api-test-dev-report
  login: parrot-api-test-dev-login
  authorizer: parrot-api-test-dev-authorizer
layers:
  None
Serverless: Removing old service artifacts from S3...
```
Una vez corriendo `serverless deploy` ya se podrá hacer peticiones a la API en la nube. Para poder hacer peticiones se necesita la api key generada en el resultado del deploy `APIKEY-PARROT-TEST` y se manda en el header `x-api-key`

## Correr serverless de manera local
```bash
serverless offline
```
El restulado del comando anterior será similar a lo siguiente:
```bash
offline: Starting Offline: dev/us-west-2.
offline: Key with token: d41d8cd98f00b204e9800998ecf8427e
offline: Remember to use x-api-key on the request headers
offline: Offline [http for lambda] listening on http://localhost:3002
offline: Function names exposed for local invocation by aws-sdk:
           * createUser: parrot-api-test-dev-createUser
           * getUsers: parrot-api-test-dev-getUsers
           * getUser: parrot-api-test-dev-getUser
           * createOrder: parrot-api-test-dev-createOrder
           * getOrders: parrot-api-test-dev-getOrders
           * getOrder: parrot-api-test-dev-getOrder
           * updateOrder: parrot-api-test-dev-updateOrder
           * deleteOrder: parrot-api-test-dev-deleteOrder
           * report: parrot-api-test-dev-report
           * login: parrot-api-test-dev-login
           * authorizer: parrot-api-test-dev-authorizer
offline: Configuring Authorization: users authorizer
offline: Configuring Authorization: users/{email} authorizer
offline: Configuring Authorization: orders authorizer
offline: Configuring Authorization: orders authorizer
offline: Configuring Authorization: orders/{id} authorizer
offline: Configuring Authorization: orders/{id} authorizer
offline: Configuring Authorization: orders/{id} authorizer
offline: Configuring Authorization: orders/report/{start_date}/{end_date} authorizer

   ┌─────────────────────────────────────────────────────────────────────────────────┐
   │                                                                                 │
   │   POST   | http://localhost:3000/dev/users                                      │
   │   POST   | http://localhost:3000/2015-03-31/functions/createUser/invocations    │
   │   GET    | http://localhost:3000/dev/users                                      │
   │   POST   | http://localhost:3000/2015-03-31/functions/getUsers/invocations      │
   │   GET    | http://localhost:3000/dev/users/{email}                              │
   │   POST   | http://localhost:3000/2015-03-31/functions/getUser/invocations       │
   │   POST   | http://localhost:3000/dev/orders                                     │
   │   POST   | http://localhost:3000/2015-03-31/functions/createOrder/invocations   │
   │   GET    | http://localhost:3000/dev/orders                                     │
   │   POST   | http://localhost:3000/2015-03-31/functions/getOrders/invocations     │
   │   GET    | http://localhost:3000/dev/orders/{id}                                │
   │   POST   | http://localhost:3000/2015-03-31/functions/getOrder/invocations      │
   │   PUT    | http://localhost:3000/dev/orders/{id}                                │
   │   POST   | http://localhost:3000/2015-03-31/functions/updateOrder/invocations   │
   │   DELETE | http://localhost:3000/dev/orders/{id}                                │
   │   POST   | http://localhost:3000/2015-03-31/functions/deleteOrder/invocations   │
   │   GET    | http://localhost:3000/dev/orders/report/{start_date}/{end_date}      │
   │   POST   | http://localhost:3000/2015-03-31/functions/report/invocations        │
   │   POST   | http://localhost:3000/dev/login                                      │
   │   POST   | http://localhost:3000/2015-03-31/functions/login/invocations         │
   │                                                                                 │
   └─────────────────────────────────────────────────────────────────────────────────┘

offline: [HTTP] server ready: http://localhost:3000 🚀
offline: 
offline: Enter "rp" to replay the last request
```
Una vez corriendo `serverless offline` ya se podrá hacer peticiones locales a la API. Para poder hacer peticiones se necesita la api key generada en el resultado del deploy `Key with token` y se manda en el header `x-api-key`

## Uso

Para hacer las llamadas a la API lo puede hacer son los siguientes comandos:


### Crear un usuario

```bash
#replace <email>, <name> & <api-key> (se obtiene al hacer deploy a la nube o cuando se corre serverless de manera local)
curl -X POST https://xxxxxxxxx/dev/users --data '{"email": "<email>", "name": "<name>"}' --header 'x-api-key: <api-key>'
```

### Hacaer login para obtener el token `(jwt)`

```bash
#replace <email> & <api-key>
curl -X POST https://xxxxxxxxx/dev/login --data '{"email": "<email>"}' --header 'x-api-key: <api-key>'
```

Output:
```bash
{"auth":true,"token":"<token>","status":"SUCCESS"}
```

### Crear una orden

```bash
#replace <client name>, <total>, <product name>, <product price>, <quantity>, <api-key> & <token> (obtenido al hacer login)
curl -X POST https:/xxxxxxxxx/dev/orders --data '{"client": "<client name>", "total": <total>, "products": [{"name": "<product name>", "price": <product price>, "quantity": <quantity>}, {"name": "<product name>", "price": <product price>, "quantity": <quantity>}]}' --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Obtener todas las ordenes

```bash
#replace <api-key> & <token>
curl -X GET https:/xxxxxxxxx/dev/orders --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Obtener una orden

```bash
#replace <id> (se obtiene en el response de crear orden), <api-key> & <token>
curl -X GET https:/xxxxxxxxx/dev/orders/<id> --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Actualizar una orden

```bash
#replace <id>, <client name>, <total>, <product name>, <product price>, <quantity>, <api-key> & <token>
curl -X PUT https:/xxxxxxxxx/dev/orders/<id> --data '{"client": "<client name>", "total": <total>, "products": [{"name": "<product name>", "price": <product price>, "quantity": <quantity>}, {"name": "<product name>", "price": <product price>, "quantity": <quantity>}]}' --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Eliminar una orden

```bash
#replace <id>, <api-key> & <token>
curl -X DELETE https:/xxxxxxxxx/dev/orders/<id> --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Obtener el reporte

```bash
#to-do: pendiente hacer el ordenamiento, se recomienda usar HiveQL
#replace <start_date>, <end_date>,  <api-key> & <token>
curl -X GET https:/xxxxxxxxx/dev/orders/report/<start_date>/<end_date> --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Obtener los usuarios

```bash
#replace <api-key> & <token>
curl -X GET https:/xxxxxxxxx/dev/users --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```

### Obtener un usuario

```bash
#replace <email>, <api-key> & <token>
curl -X GET https:/xxxxxxxxx/dev/users/<email> --header 'x-api-key: <api-key>' --header 'authorizationToken:Bearer <token>'
```
