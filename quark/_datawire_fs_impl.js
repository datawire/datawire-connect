(function () {
    "use strict";

    var os = require('os');
    var fs = require('fs');

    var quark = require('quark').quark;

    var _datawire_fs = (function () {
        function _datawire_fs() {}

        _datawire_fs.userHomeDir = function () {
            return os.homedir();
        };

        _datawire_fs.fileContents = function (path) {
            try {
                return fs.readFileSync(path, 'utf-8');
            }
            catch (e) {
                var runtime = quark.concurrent.Context.runtime();
                runtime.fail("failure reading " + path + ": " + e)
            }
        };

        return _datawire_fs;
    })();

    module.exports = _datawire_fs;
})();
