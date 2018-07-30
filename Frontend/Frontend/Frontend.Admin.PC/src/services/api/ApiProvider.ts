class ApiProvider {
    isMock: boolean = true;


    constructor() {
        if (this.isMock) {

        } else {

        }
    }
}

export const api = new ApiProvider();