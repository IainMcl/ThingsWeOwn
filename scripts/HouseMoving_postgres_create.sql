CREATE TABLE-- IF NOT EXISTS
"House" (
	"House_pk" SERIAL,
	"HouseName" VARCHAR(255) NOT NULL,
	"Room" VARCHAR(255) NOT NULL--,
	--CONSTRAINT "House_pk" PRIMARY KEY ("HouseName", "Room")
) WITH (
  OIDS=FALSE
);



CREATE TABLE-- IF NOT EXISTS
"Contents" (
	"House_pk" VARCHAR(255) NOT NULL,
	"ItemName" VARCHAR(255) NOT NULL
) WITH (
  OIDS=FALSE
);



CREATE TABLE-- IF NOT EXISTS
"Item" (
	"ItemName" VARCHAR(255) NOT NULL,
	"Quantity" integer NOT NULL DEFAULT '1',
	"Size" VARCHAR(255) NOT NULL DEFAULT 'medium',
	"Priority" integer NOT NULL DEFAULT '0',
	"Fragile" BOOLEAN NOT NULL DEFAULT 'false',
	"Owned" BOOLEAN NOT NULL DEFAULT 'true',
	"Moved" BOOLEAN NOT NULL DEFAULT 'false',
	"Keeping" BOOLEAN NOT NULL DEFAULT 'true',
	"Value" integer NOT NULL,
	"Owner" VARCHAR(255) NOT NULL,
	"Notes" VARCHAR(255),
	CONSTRAINT "Item_pk" PRIMARY KEY ("ItemName")
) WITH (
  OIDS=FALSE
);



CREATE TABLE-- IF NOT EXISTS 
"Person" (
	"Name" VARCHAR(255) NOT NULL,
	"Priority" integer NOT NULL DEFAULT '0',
	CONSTRAINT "Person_pk" PRIMARY KEY ("Name")
) WITH (
  OIDS=FALSE
);


ALTER TABLE "Contents" DROP CONSTRAINT IF EXISTS "Contents_fk0";
ALTER TABLE "Contents" ADD CONSTRAINT "Contents_fk0" FOREIGN KEY ("House_pk") REFERENCES "House"("Room");
ALTER TABLE "Contents" DROP CONSTRAINT IF EXISTS "Contents_fk1";
ALTER TABLE "Contents" ADD CONSTRAINT "Contents_fk1" FOREIGN KEY ("ItemName") REFERENCES "Item"("ItemName");

ALTER TABLE "Item" DROP CONSTRAINT IF EXISTS "Item_fk0";
ALTER TABLE "Item" ADD CONSTRAINT "Item_fk0" FOREIGN KEY ("Owner") REFERENCES "Person"("Name");


