const fs = require('fs').promises;

async function main() {

    const database = await readDatabase('base.json');
    const faturamento = database.faturamento
    
    const biggerThanAverage = await biggerAverage(faturamento)
    
    console.log(`O menor valor é ${await findMinValue(faturamento)}`);
    console.log(`O maior valor é ${await findMaxValue(faturamento)}`);
    console.log('Os dias com faturamento maior que a média são: ');
    for (const day of biggerThanAverage) {
    console.log(day.dia);
    }
}

async function readDatabase(filePath) {
  const data = await fs.readFile(filePath);
  return JSON.parse(data);
}
async function findMinValue(faturamento) {
    const validate = faturamento
    .filter(item => item.valor > 0)
    .map(item => item.valor)

    return Math.min(...validate)
}
async function findMaxValue(faturamento) {
    const validate = faturamento
        .filter(item => item.valor > 0)
        .map(item => item.valor)

    return Math.max(...validate)
}
async function biggerAverage(faturamento) {
    const totalIncome = faturamento.reduce((total, day) => total + day.valor, 0);
    const validate = faturamento.filter(item => item.valor > 0).length;
    const average = totalIncome / validate;
  
    const biggerThanAverage = faturamento.filter(day => day.valor > average);
    
    return biggerThanAverage;
}

main();