import QtQml 2.0
import QOwnNotesTypes 1.0

Script {
    /**
        * Will be run when the scripting engine initializes
        */
       function init() {
	       script.log("Shared started");
       }

       function onNoteStored(note) {
	       script.startDetachedProcess("update_public_shares", [note.fullNoteFilePath]);
       }
}
