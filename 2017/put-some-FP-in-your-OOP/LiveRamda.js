const R = require('ramda');

const hopes = { 
    speaker:"Michael Richardson", 
    topic: "Put Some FP in your OOP", 
    quality: 10}
const qualityLens = R.lensPath(["quality"]);

const reality = R.set(qualityLens, 2 , hopes);
reality

const hopefulQuality = R.view(qualityLens, hopes);
const realQuality = R.view(qualityLens, reality);

hopefulQuality
realQuality



const getQuality = R.view(qualityLens);

const hopefulQualityCurried = getQuality(hopes);
const realQualityCurried = getQuality(reality);


hopefulQualityCurried
realQualityCurried


