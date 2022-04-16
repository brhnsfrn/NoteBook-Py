CREATE TABLE IF NOT EXISTS notes (
    id char(36) PRIMARY KEY,
    content TEXT NOT NULL,
    created_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TRIGGER IF NOT EXISTS GenerateUUID
AFTER INSERT ON notes
FOR EACH ROW
WHEN (NEW.id IS NULL)
BEGIN
   UPDATE notes SET id = (select hex( randomblob(4)) || '-' || hex( randomblob(2))
             || '-' || '4' || substr( hex( randomblob(2)), 2) || '-'
             || substr('AB89', 1 + (abs(random()) % 4) , 1)  ||
             substr(hex(randomblob(2)), 2) || '-' || hex(randomblob(6)) ) WHERE rowid = NEW.rowid;
END;