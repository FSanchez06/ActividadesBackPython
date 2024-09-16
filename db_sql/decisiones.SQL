CREATE DATABASE unidad_productiva;
USE unidad_productiva;

CREATE TABLE enfermedades (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  caracteristicas TEXT,
  tratamiento TEXT
);

select * from enfermedades;

INSERT INTO enfermedades (nombre, caracteristicas, tratamiento) VALUES 
('Mildiu', 'Humedad alta, manchas en hojas, crecimiento lento', 'Aplicar fungicidas y mejorar la ventilación.'),
('Pudrición de raíz', 'Hojas amarillas, marchitamiento, suelo muy húmedo', 'Reducir riego y aplicar fungicidas sistémicos.'),
('Oídio', 'Manchas blancas en hojas, clima seco y cálido', 'Aplicar fungicidas específicos para oídio.'),
('Virus del mosaico', 'Hojas con manchas amarillas, deformación de hojas', 'Eliminar plantas infectadas y controlar pulgones.'),
('Antracnosis', 'Manchas oscuras en frutas y hojas, condiciones húmedas', 'Aplicar fungicidas y eliminar restos de plantas infectadas.');
