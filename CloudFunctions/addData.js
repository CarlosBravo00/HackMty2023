const AWS = require("aws-sdk");
const documentClient = new AWS.DynamoDB.DocumentClient();

function subtractHours(numOfHours, date = new Date()) {
  date.setHours(date.getHours() - numOfHours);

  return date;
}

exports.handler = async (event, context) => {
  console.log(event);
  const args = JSON.parse(event.body);
  console.log(args);

  let insertParams = {
    TableName: "plant_logs",
  };

  const date = subtractHours(6);
  const newItem = {
    id: context.awsRequestId,
    light: args.light,
    temperature: args.temperature,
    water: args.water,
    date: date.toISOString(),
  };
  insertParams.Item = newItem;
  await documentClient.put(insertParams).promise();

  const response = {
    statusCode: 200,
    body: JSON.stringify(newItem),
  };
  return response;
};
