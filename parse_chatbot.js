const fs = require('fs');

const html = fs.readFileSync('chatbot.html', 'utf-8');

function extractData(varName) {
    // Basic extraction using regex
    const regex = new RegExp(`const\\s+${varName}\\s*=\\s*(\\[[\\s\\S]*?\\]|\\{[\\s\\S]*?\\});`, 'i');
    const match = html.match(regex);
    if (!match) {
        // Try another format if it's SPECIFIC_QA etc
        return null;
    }
    
    let objStr = match[1];
    
    // Quick and dirty eval to get the object
    // Need to handle regexes inside SPECIFIC_QA
    if (varName === 'FAQ_REGEX_DATA') {
        // We can't eval regexes directly into JSON
        // Convert /pattern/i to string
        objStr = objStr.replace(/pattern:\s*(\/.*?\/i?)/g, 'pattern: "$1"');
    }
    
    let obj;
    try {
        obj = eval('(' + objStr + ')');
    } catch (e) {
        console.error("Error evaluating " + varName, e);
        return null;
    }
    return obj;
}

const knowledgeBase = extractData('SUKU_DATA');
const wisataData = extractData('WISATA_DATA');
const alatMusikData = extractData('ALAT_MUSIK_DATA');
const specificQA = extractData('FAQ_REGEX_DATA');
const categories = extractData('CATEGORIES');
const categoryNames = extractData('CATEGORY_NAMES');

fs.writeFileSync('chatbot_data.json', JSON.stringify({
    KNOWLEDGE_BASE: knowledgeBase,
    WISATA_DATA: wisataData,
    ALAT_MUSIK_DATA: alatMusikData,
    SPECIFIC_QA: specificQA,
    CATEGORIES: categories,
    CATEGORY_NAMES: categoryNames
}, null, 2));

console.log("Data extracted to chatbot_data.json");
