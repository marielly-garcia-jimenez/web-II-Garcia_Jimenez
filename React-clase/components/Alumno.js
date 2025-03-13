const { useState } = React;

function Alumno({ alumno }) {
    const [visible, setVisible] = useState(true);

    const alternarVisibilidad = () => {
        setVisible(prevVisible => !prevVisible);
    };
    
    return (
        <div>
            
            {visible && (
                <div>
                    <p>Nombre: {alumno.nombre}</p>
                    <p>Notas: {alumno.notas}</p>
                    <p>Asignatura: {alumno.asignatura}</p>
                </div>
            )}

            <button onClick={alternarVisibilidad}>
                {visible ? 'Ocultar' : 'Mostrar'} info: {alumno.nombre}
            </button>
        </div>
    );
}

window.Alumno = Alumno;