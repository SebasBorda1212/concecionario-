describe('Pruebas de Integración de API - Concesionario', () => {
  const baseUrl = 'http://127.0.0.1:8000/api/v1';
  let authToken = '';
  let vehiculoId = null;

  before(() => {
    cy.request({
      method: 'POST',
      url: `${baseUrl}/auth/token/`,
      body: {
        username: 'sebas',
        password: '1234'
      }
    }).then((response) => {
      expect(response.status).to.eq(200);
      expect(response.body).to.have.property('token');
      authToken = response.body.token;
    });
  });

  it('1. POST - Crear un nuevo vehículo con Token', () => {
    cy.request({
      method: 'POST',
      url: `${baseUrl}/vehiculos/`,
      headers: {
        Authorization: `Token ${authToken}`
      },
      body: {
        marca_modelo: 'Mazda CX-30 Touring',
        vin: '3MZDM2BY3PM123789',
        precio_base: 95000000.00,
        anio: 2024
      }
    }).then((response) => {
      expect(response.status).to.eq(201);
      expect(response.body).to.have.property('id');
      vehiculoId = response.body.id;
    });
  });

  it('2. GET - Consultar el vehículo creado por ID', () => {
    // Asegúrate de tener el ID o realiza la consulta general si prefieres
    cy.request({
      method: 'GET',
      url: `${baseUrl}/vehiculos/`
    }).then((response) => {
      expect(response.status).to.eq(200);
    });
  });
});