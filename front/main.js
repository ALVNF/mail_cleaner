//Test Function
function callDummy() {
  var data = document.getElementById("mailCleaner").value;
  eel.dummy(data)(function (ret) {
    console.log(ret);
  });
}

//Call Add to list function
function callAdd() {
  var mail2Add = document.getElementById("mail2add").value;
  eel.add2List(mail2Add)(function (ret) {
    openConsole(ret);
    document.getElementById("mail2add").value = "";
  });
}

//Call Remove from list function
function callRemove() {
  var mail2Rem = document.getElementById("mail2add").value;
  eel.removeFromList(mail2Rem)(function (ret) {
    openConsole(ret);
    document.getElementById("mail2add").value = "";
  });
}

//Call Cleaner from list function
function callCleaner() {
  var mail = document.getElementById("mailCleaner").value;
  var passwd = document.getElementById("mailPasswd").value;
  openConsole("Calling Cleaner, please wait until finish. \n");
  eel.cleaner(
    mail,
    passwd
  )(async function (ret) {
    await openConsole(ret);
  });
}

//Open Side Navigation
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}
//Close Side Navigation
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft = "0";
}

//Open console
function openConsole(data) {
  document.getElementById("consoleContainer").style.display = "block";
  document.getElementById("container").style.top = "285px";
  document.getElementById("console").value += data;
}

//Render Cleaner Container
function renderMain() {
  document.getElementById("AddRemoveContainer").style.display = "none";
  document.getElementById("showListContainer").style.display = "none";
  document.getElementById("consoleContainer").style.display = "none";

  document.getElementById("container").style.top = "350px";
  document.getElementById("container").style.display = "block";

  document.getElementById("addRemoveReff").style.boxShadow = "";
  document.getElementById("listReff").style.boxShadow = "";
  document.getElementById("mainReff").style.boxShadow = "0px 0px 55px #60ede3";
}

//Render Add Remove Container
function renderAdd() {
  document.getElementById("container").style.display = "none";
  document.getElementById("showListContainer").style.display = "none";
  document.getElementById("consoleContainer").style.display = "none";

  document.getElementById("AddRemoveContainer").style.top = "350px";
  document.getElementById("AddRemoveContainer").style.display = "block";

  document.getElementById("mainReff").style.boxShadow = "";
  document.getElementById("listReff").style.boxShadow = "";
  document.getElementById("addRemoveReff").style.boxShadow =
    "0px 0px 55px #60ede3";
}

//Render List Container
function renderList() {
  document.getElementById("container").style.display = "none";
  document.getElementById("AddRemoveContainer").style.display = "none";
  document.getElementById("consoleContainer").style.display = "none";

  document.getElementById("showListContainer").style.display = "block";

  document.getElementById("mainReff").style.boxShadow = "";
  document.getElementById("addRemoveReff").style.boxShadow = "";
  document.getElementById("listReff").style.boxShadow = "0px 0px 55px #60ede3";

  eel.readList()(function (ret) {
    document.getElementById("mailList").value = ret;
  });
}
