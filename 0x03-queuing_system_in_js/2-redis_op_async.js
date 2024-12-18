import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log("Redis client connected to the server")
})

client.on('error', err => {
    console.log("Redis client not connected to the server: ERROR_MESSAGE", err)
})

function setNewSchool(schoolName, value){
    client.set(schoolName, value, print)
}

async function displaySchoolValue(schoolName){
    try {
        const value = await getAsync(schoolName);
        console.log(value)
    } catch (error){
        console.error('Error fetching value:', error)
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');