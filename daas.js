const ptypes = [
    "fact",
    "value",
    "policy"
];

const axios = require('axios')

async function get_response(locution) {
    response = { "locutions": [] }

    r = await axios.post('http://proptest-ws:8199/process', {
        string: locution['content']
    })
    .then(res => {
        agent = "IntentRecognitionAgent";
        rvals = JSON.parse(res['data']);
        console.log(rvals);
        mval = 0;
        mlbl = -1;
        for (var i=0 ; i<rvals.length ; i++) {
            if(rvals[i] > mval){
                mval = rvals[i];
                mlbl = i;
            } 
        }
        rtext = locution['type'] + '-' + ptypes[mlbl] + '(' + mval.toFixed(2) + ')';
        move = {"speaker": agent, "content": rtext};
        response['locutions'].push(move);
        return response;
    })
    .catch(error => {
        console.error(error)
    })

    return r;
}

module.exports.get_response = get_response;
