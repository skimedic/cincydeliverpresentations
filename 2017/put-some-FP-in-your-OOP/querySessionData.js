const R = require('ramda');

const sessionData = require('./session-data.json');

const webDevTalks = sessionData.filter(session => session.Genre === "Web Development");
webDevTalks

const lens = R.lensPath([0, "Speaker"]);
const firstSpeakerName = R.view(lens, webDevTalks);

console.log(firstSpeakerName + " is an AWESOME speaker!");

const newLens = R.lensPath([5, "Speaker"]);
const updatedTalks = R.set(newLens, "Michael Richardson", webDevTalks);
updatedTalks

console.log(webDevTalks)
