import React, { useContext } from "react";
import { Context } from "../store/appContext";
import "../../styles/home.css";

export const Registro = () => {
  const { store, actions } = useContext(Context);

  return (
    <div className="formulario card w-50">
      <div className="card-body">
        <div className="row">
          <div className="img col"></div>
          <form className="col">
            <div className="input mb-3">
              <label htmlFor="exampleInputEmail1" className="form-label">
                Email
              </label>
              <input
                type="email"
                className="form-control"
                id="exampleInputEmail1"
                aria-describedby="emailHelp"
              />
            </div>
            <div className="input mb-3">
              <label htmlFor="exampleInputPassword1" className="form-label">
                Contraseña
              </label>
              <input
                type="password"
                className="form-control"
                id="exampleInputPassword1"
              />
			  <div id="passwordHelp" className="form-text">
                Debe tener entre 5 y 8 caracteres. 
            </div>
            </div>
            
            <button type="submit" className="input btn btn-primary">
              Registrarme
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};
