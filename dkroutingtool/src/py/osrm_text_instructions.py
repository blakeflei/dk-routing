import bond

javascript = bond.make_bond("JavaScript")

javascript.eval_block("var osrm = require('osrm-text-instructions')('v5');")

javascript.eval_block("function instruct(response) {var instructions = []; response.legs.forEach(function(leg) {leg.steps.forEach(function(step){instructions.push(osrm.compile('en', step))});}); return instructions};")

def get_instructions(parsed):
	instructions = javascript.call("instruct", parsed["routes"][0])
	return instructions

"""
not used currently
deps:
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -

RUN apt-get -y install nodejs

RUN npm install osrm-text-instructions

"""
