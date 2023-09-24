const AWS = require("aws-sdk");
const documentClient = new AWS.DynamoDB.DocumentClient();

exports.handler = async (event) => {
  const params = {
    TableName: "plant_logs",
    ProjectionExpression: "water, temperature, light, #date", // Include the fields you want here, excluding 'id'.
    ExpressionAttributeNames: { "#date": "date" } // Use ExpressionAttributeNames if any of your field names are reserved words
  };

  let itemsList = [];
  let data;
  do {
    data = await documentClient.scan(params).promise();
    itemsList = itemsList.concat(data.Items);
    params.ExclusiveStartKey = data.LastEvaluatedKey;
  } while (data.LastEvaluatedKey);

  console.log(itemsList);

  const sortedList = itemsList.sort((a, b) => {
    let dateA = new Date(a["date"]);
    let dateB = new Date(b["date"]);
    if (dateA < dateB) {
      return -1;
    } else if (dateA > dateB) {
      return 1;
    }
    return 0;
  });

  console.log(sortedList);

  const response = {
    statusCode: 200,
    body: JSON.stringify(sortedList.slice(-120)),
  };

  return response;
};
