import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Home } from "./pages/home";
import { FrontPage } from "./pages/FrontPage";
import { CompanyRegister } from "./pages/CompanyRegister";
import { UserRegister } from "./pages/UserRegister";
import { CompanyLogin } from "./pages/CompanyLogin";
import { UserLogin } from "./pages/UserLogin";
import { AdminLogin } from "./pages/AdminLogin";
import { UserProfile } from "./pages/UserProfile";
import { CompanyProfile } from "./pages/CompanyProfile ";
import { Jobs } from "./pages/Jobs";
import { MyJobsApply } from "./pages/MyJobsApply";
import { MyPostsCompany } from "./pages/MyPostsCompany";
import { Demo } from "./pages/demo";
import { Single } from "./pages/single";
import injectContext from "./store/appContext";
import { AdminRegisterPrueba } from "./pages/AdminRegisterPrueba";
import { Navbar2 } from "./component/navbar2";

import { Navbar } from "./component/Navbar";
import { Footer } from "./component/footer";
import { StudentApplications } from "./pages/StudentApplications";
import { ApplyCompany } from "./pages/ApplyCompany";

//create your first component
const Layout = () => {
  //the basename is used when your project is published in a subdirectory and not in the root of the domain
  // you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
  const basename = process.env.BASENAME || "";

  return (
    <div>
      <BrowserRouter basename={basename}>
        <ScrollToTop>
          <Navbar2 />
          <Switch>
            <Route exact path="/">
              <FrontPage />
            </Route>
            <Route exact path="/RegistroEmpresa">
              <CompanyRegister />
            </Route>
            <Route exact path="/RegistroAlumno">
              <UserRegister />
            </Route>
            <Route exact path="/RegistroAdmin">
              <AdminRegisterPrueba />
            </Route>
            <Route exact path="/AccesoEmpresa">
              <CompanyLogin />
            </Route>
            <Route exact path="/AccesoAlumno">
              <UserLogin />
            </Route>
            <Route exact path="/PerfilEmpresa">
              <CompanyProfile />
            </Route>
            <Route exact path="/PerfilAlumno">
              <UserProfile />
            </Route>
            <Route exact path="/AccesoAdmin">
              <AdminLogin />
            </Route>
            <Route exact path="/Buscador">
              <Jobs />
            </Route>
            <Route exact path="/TusPostulaciones">
              <MyJobsApply />
            </Route>
            <Route exact path="/TusOfertas">
              <MyPostsCompany />
            </Route>
            <Route exact path="/single/:theid">
              <Single />
            </Route>
            <Route exact path="/MisPostulaciones">
              <StudentApplications />
            </Route>
            <Route exact path="/PublicacionEmpresa">
              <ApplyCompany />
            </Route>
            <Route>
              <h1>Not found!</h1>
            </Route>
          </Switch>
          <Footer />
        </ScrollToTop>
      </BrowserRouter>
    </div>
  );
};

export default injectContext(Layout);
