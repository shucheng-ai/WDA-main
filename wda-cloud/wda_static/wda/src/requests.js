import axios from 'axios';

let timeout = 1000 * 60 * 2; // 60*2秒超时

const ERROR_MSG = {
    1: 'Server not responding, try again later.\n', // 服务器超时 === 504
};

const baseRequests = async (api, data, method, config) => {
    method = method ? method : 'get';
    // let now = new Date();
    const promise = new Promise(function (resolve, reject) {
        let axios_config = {
            method: method,
            url: api,
            timeout: timeout,
            data: data,
        };
        if (config) {
            axios_config.config = config;
        }
        axios(axios_config).then(
            (res) => {
                resolve(res);
            },
            () => {
                console.warn(`${api} request fail.`);
                reject({status: -1, err_msg: ERROR_MSG});
            }
        );
    });
    return promise;
};

const RequestGET = function (api, data) {
    return baseRequests(api, data, 'get');
};

const RequestPOST = function (api, data) {
    return baseRequests(api, data, 'post');
};

const RequestPUT = function (api, data) {
    return baseRequests(api, data, 'put');
};

const RequestDELETE = function (api, data) {
    return baseRequests(api, data, 'delete');
};

const RequestUPLOAD = (api, data, config) => {
    return baseRequests(api, data, 'post', config);
};

const Request = {
    get: RequestGET,
    post: RequestPOST,
    put: RequestPUT,
    delete: RequestDELETE,
    upload: RequestUPLOAD,
};

export {RequestGET, RequestPOST, RequestPUT, RequestDELETE, RequestUPLOAD};
export default Request;
