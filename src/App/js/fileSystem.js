const fs = require('fs');

class gstvsFileEnt {
    name = "";
    fullPath = "";
}

class gstvDirEnt {
    name = "";
    fullPath = "";
}

class gstvsFile {
    
    static getFullDirStructure(localPath) {
        fs.stat(localPath, function(err, stats) {
            console.log(localPath);
            console.log();
            console.log(stats);
            console.log();
        });
    }

    static getDirContents(localPath, cb) {
        fs.readdir(localPath, {withFileTypes:true}, function(err, files){
            console.log(gstvsGit.tst);            

            var filteredFiles = files.filter(function (el) {
                if(el.name.startsWith(".git")) return(false);
                return(true);
            });
            var entities = [];
            filteredFiles.forEach(function(el){
                var newEnt = new gstvsFileEnt();
                newEnt.name = el.name;
                entities.push(newEnt);
            });

            console.log(entities);
        });
    }
}

