//login
const jwt = require("jsonwebtoken");
const AWS = require('aws-sdk');


if(process.env.IS_OFFLINE != undefined && process.env.IS_OFFLINE == "true") {
	AWS.config.update({region: 'us-west-2', endpoint: "http://localhost:8000"});
} else {
	AWS.config.update({region: 'us-west-2'});
}

const docClient = new AWS.DynamoDB.DocumentClient();

exports.handler = async function(event, context, callback) {
	const requestBody = JSON.parse(event.body);

    if(requestBody.email == undefined || requestBody.email == null || requestBody.email == "") {
		return {
			statusCode: 401,
			headers: { "Content-Type": "text/plain" },
			body: {}
		};
	} else {
		const data = await getItem(requestBody.email);
		
		if(data == false) {
			return {
				statusCode: 401,
				headers: { "Content-Type": "text/plain" },
				body: {}
			};
		} else {
			if('Item' in data){
				return login(requestBody.email)
					.then(session => ({
						statusCode: 200,
						body: JSON.stringify(session)
					}))
					.catch(err => {
						console.log({ err });
						
						return {
							statusCode: 401,
							headers: { "Content-Type": "text/plain" },
							body: {}
						};
					});
			} else {
				return {
					statusCode: 401,
					headers: { "Content-Type": "text/plain" },
					body: {}
				};
			}
		}
	}
};

async function getItem(email) {
	const params = {
		TableName : process.env.DYNAMODB_TABLE_USERS,
		Key: {
			email: email
		}
	}

	try {
		const data = await docClient.get(params).promise();
		return data;
	} catch (err) {
		return false;
	}
}

async function login(email) {
  try {
      const token = await signToken(email);
      return Promise.resolve({ auth: true, token: token, status: "SUCCESS" });
  } catch (err) {
    console.info("Error login", err);
    return Promise.reject(new Error(err));
  }
}

async function signToken(email) {
	const secret = Buffer.from(process.env.JWT_SECRET, "base64");

	return jwt.sign({ email: email}, secret, {
		expiresIn: 86400
	});
}
