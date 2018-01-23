import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

function findIndexOfStocks(symbol) {
  return state.stocks.findIndex(stock => {
    return stock.symbol === symbol
  })
}

const state = {
  isLogInModal: false,
  isConfirmModal: false,
  isRegisterModal: false,
  nextActionInfo: null,
  stocks: null,
  step: 1,
  cash: null,
  username: null,
  category: null
}

const mutations = {
  CLOSE_MODAL(state) {
    state.isLogInModal = false
    state.isConfirmModal = false
    state.isRegisterModal = false
  },
  OPEN_LOG_IN_MODAL(state) {
    state.isLogInModal = true
  },
  OPEN_CONFIRM_MODAL(state, nextActionInfo) {
    state.isConfirmModal = true
    state.nextActionInfo = nextActionInfo
  },
  OPEN_REGISTER_MODAL(state) {
    state.isRegisterModal = true
  },
  UPDATE_STOCK(state, stocks) {
    for( let stock in stocks) {
      let stockIndex = findIndexOfStocks(stock.symbol)

      state.stocks[stockIndex].amount = stock.amount
      state.stocks[stockIndex].averagePrice = stock.averagePrice
    }
  },
  SET_STOCK(state, stocks) {
    state.stocks = stocks
  },
  SET_USERNAME(state, username) {
    state.username = username
  },
  SET_STEP(state, step) {
    state.step = step
  },
  SET_CASH(state, cash) {
    state.cash = cash
  },
  SET_CURRENT_CATEGORY(state, category) {
    state.category = category
  }
}

const actions = {
  closeModal: ({ commit }) => commit('CLOSE_MODAL'),
  openLogInModal: ({ commit }) => commit('OPEN_LOG_IN_MODAL'),
  openRegisterModal: ({ commit }) => commit('OPEN_REGISTER_MODAL'),
  openConfirmModal: ({ commit }, nextActionInfo) => commit('OPEN_CONFIRM_MODAL', nextActionInfo),
  updateStock: ({ commit }, stocks) => commit('UPDATE_STOCK', stocks),
  setStock: ({ commit }, stocks) => commit('SET_STOCK', stocks),
  setUsername: ({ commit }, username) => commit('SET_USERNAME', username),
  setStep: ({ commit }, step) => commit('SET_STEP', step),
  setCash: ({ commit }, cash) => commit('SET_CASH', cash),
  setCurrentCategory: ({ commit }, category) => commit('SET_CURRENT_CATEGORY', category)
}

const getters = {
  getIsModalOpen: state => { return state.isConfirmModal || state.isLogInModal || state.isRegisterModal },
  getIsLogInModal: state => state.isLogInModal,
  getIsRegisterModal: state => state.isRegisterModal,
  getIsConfirmModal: state => state.isConfirmModal,
  getStock: state => state.stocks,
  getNextActionInfo: state => state.nextActionInfo,
  getUsername: state => state.username,
  getCash: state => state.cash,
  getStep: state => state.step,
  getCurrentCategory: state => state.category,
  isLoggedIn: state => state.username !== null
}

export default new Vuex.Store({
  state,
  getters,
  mutations,
  actions
})
