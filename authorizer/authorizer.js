// A simple token-based authorizer
const jwt = require("jsonwebtoken");

exports.handler = async function(event, context, callback) {
    const token = event.authorizationToken.replace("Bearer ", "");
	const methodArn = event.methodArn;

	if (!token || !methodArn) return callback(null, "Unauthorized");

	const secret = Buffer.from(process.env.JWT_SECRET, "base64");
	
	// verifies token
	const decoded = jwt.verify(token, secret);

	if (decoded && decoded.email) {
		callback(null, generatePolicy('user', 'Allow', event.methodArn, decoded.email));
	} else {
		callback(null, generatePolicy('user', 'Deny', event.methodArn, null));
	}
};

// Help function to generate an IAM policy
var generatePolicy = function(principalId, effect, resource, data) {
    var authResponse = {};
    
    authResponse.principalId = principalId;
    if (effect && resource) {
        var policyDocument = {};
        policyDocument.Version = '2012-10-17'; 
        policyDocument.Statement = [];
        var statementOne = {};
        statementOne.Action = 'execute-api:Invoke'; 
        statementOne.Effect = effect;
        statementOne.Resource = resource;
        policyDocument.Statement[0] = statementOne;
        authResponse.policyDocument = policyDocument;
    }
    
    authResponse.context = {
        "user_email": data,
    };
    return authResponse;
}
